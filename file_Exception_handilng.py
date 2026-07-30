# try:
#     file = open("file_handling_practice.txt", "r")
#     print(file.read())
#     file.close()

# except FileNotFoundError:
#     print("Error: File not found.")


# try:
#     with open("file_handling_practice.txt", "r") as file:
#         lines = file.readlines()

#     print("Total Lines:", len(lines))

# except FileNotFoundError:
#     print("File not found.")




# try:
#     with open("file_handling_practice.txt", "a") as file:
#         file.write("\nThis line is added using append mode.")

#     print("Data written successfully.")

# except Exception as e:
#     print("Error:", e)