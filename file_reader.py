try:
    with open("sample.txt","r") as file:
        content = file.read()
        print("\nFILE CONTENT:")
        print(content)
    
except FileNotFoundError:
    print("Error: file not found")

except PermissionError:
    print("Error: permission denied")

except Exception as e:
    print(f"Unexpected error: {e}")

