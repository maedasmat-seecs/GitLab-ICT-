# storage_estimator.py
# Estimates how much cloud storage is needed
//A NEW CHANGE

def estimate_storage(num_files, avg_size_mb):
    total_mb = num_files * avg_size_mb
    return total_mb

def main():
    print("Storage Estimator")
    num_files = int(input("Number of files: "))
    avg_size = float(input("Average file size (MB): "))
    total = estimate_storage(num_files, avg_size)
    print("Total storage needed:", total, "MB")

main()
print("Total storage needed:", total, "MB")
print("Total in GB:", round(total / 1024, 2), "GB")