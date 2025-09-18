import boto3
import hashlib

# ---------- CONFIG ----------
BUCKET_NAME = "cloud-dedupe-project"  # change to your bucket name
REGION = "ap-south-1"
DUPLICATE_FOLDER = "duplicates/"      # folder to store duplicates
# ----------------------------

# Initialize S3 client
s3 = boto3.client("s3", region_name=REGION)

def get_file_hash(bucket, key):
    """Download file in memory and compute MD5 hash."""
    obj = s3.get_object(Bucket=bucket, Key=key)
    file_data = obj["Body"].read()
    return hashlib.md5(file_data).hexdigest()

def find_and_move_duplicates(bucket):
    print(f"Scanning bucket: {bucket}")

    # Get all objects
    response = s3.list_objects_v2(Bucket=bucket)
    if "Contents" not in response:
        print("No files found in bucket.")
        return

    seen_hashes = {}
    duplicates = []

    for item in response["Contents"]:
        key = item["Key"]

        # Skip already moved files inside duplicates folder
        if key.startswith(DUPLICATE_FOLDER):
            continue

        print(f"Checking file: {key}")

        file_hash = get_file_hash(bucket, key)

        if file_hash in seen_hashes:
            print(f"Duplicate found: {key} (same as {seen_hashes[file_hash]})")
            duplicates.append(key)
        else:
            seen_hashes[file_hash] = key

    # Move duplicates
    if duplicates:
        print("\nMoving duplicates to 'duplicates/' folder...")
        for dup in duplicates:
            new_key = DUPLICATE_FOLDER + dup.split("/")[-1]  # keep filename
            # Copy to duplicates folder
            s3.copy_object(Bucket=bucket, CopySource={"Bucket": bucket, "Key": dup}, Key=new_key)
            # Delete original
            s3.delete_object(Bucket=bucket, Key=dup)
            print(f"Moved: {dup} → {new_key}")
    else:
        print("No duplicates found!")

if __name__ == "__main__":
    find_and_move_duplicates(BUCKET_NAME)
