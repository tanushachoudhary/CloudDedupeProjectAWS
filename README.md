# ☁️ Cloud Storage Data Redundancy Removal

## 📌 Abstract

This project demonstrates a **Data Deduplication System** for cloud storage using **AWS S3 and Python (Boto3)**. It scans files stored in an S3 bucket, computes their **hash values (MD5)**, identifies duplicate files, and moves duplicates into a dedicated `duplicates/` folder. This reduces **storage cost** and ensures **efficient data management** in cloud environments.

---

## 🎯 Purpose of Work

* To minimize cloud storage usage by detecting and handling duplicate files.
* To demonstrate practical **cloud computing concepts** using AWS services.
* To automate redundancy removal with a simple Python script.

---

## 🏗️ System Architecture

```plaintext
+------------+          +------------+          +----------------+
|   Client   |  --->    |   AWS S3   |  --->    | Deduplication  |
|  (Python)  |          |   Bucket   |          |   Script       |
+------------+          +------------+          +----------------+
                               |
                               v
                        +---------------+
                        | Duplicates/   |
                        | (Moved Files) |
                        +---------------+
```

---

## ⚙️ Hardware & Software Requirements

**Hardware**

* Any laptop/desktop with internet access

**Software**

* Python 3.x
* AWS CLI
* Boto3 library (`pip install boto3`)
* AWS Free Tier account
* S3 bucket

---

## 🛠️ Working Steps

1. **Create an AWS S3 bucket** (e.g., `cloud-dedupe-project`).
2. **Upload files** (including duplicates) into the bucket.
3. **Run Python script** (`dedupe.py`):

   * Computes hash of each file.
   * Identifies duplicates.
   * Moves duplicates into `/duplicates/` folder.
4. **Check results** in AWS S3 Console.

---

## 🖼️ Screenshots

### ✅ Before Running Script

<img width="1914" height="805" alt="Screenshot 2025-09-09 104028" src="https://github.com/user-attachments/assets/5f5cb279-cbad-4e4c-b35c-36ea757e9ce5" />


### ✅ After Running Script


<img width="1561" height="632" alt="Screenshot 2025-09-09 104127" src="https://github.com/user-attachments/assets/0cd72a4c-8797-4b60-9e07-8ae920ea6f4f" />
<img width="1529" height="511" alt="Screenshot 2025-09-09 104138" src="https://github.com/user-attachments/assets/3a074db2-f96c-4fbd-a132-caac6c9fbc0d" />

---

## 🧑‍💻 Technology Used

* **AWS S3 (Storage)**
* **Python (Boto3 SDK)**
* **Hashing (MD5)**

---

## ✅ Conclusion

The project successfully demonstrates how to **identify and remove redundant data** in cloud storage using a simple Python script and AWS S3. This technique optimizes storage utilization, reduces costs, and can be extended for large-scale enterprise systems.

---

## 🔗 References

* [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
* [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* [AWS Free Tier](https://aws.amazon.com/free/)

---

⚡ *This project runs fully on the AWS Free Tier and is safe for academic/learning purposes.*


Do you also want me to prepare a **1-page project summary version** (like for your submission sheet) based on this README?
