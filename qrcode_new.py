import qrcode

def generate_qr_code():
    print("Welcome to the Enhanced QR Code Generator!")
    print("Please select the type of QR code:")
    print("1. Plain Text")
    print("2. URL Link")
    print("3. Contact Information (vCard)")

    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        content = input("Enter the text content for the QR code: ")
    elif choice == "2":
        url = input("Enter the URL link for the QR code: ")
        content = url.strip()  # Remove extra spaces
    elif choice == "3":
        print("Enter contact information:")
        name = input("Name: ")
        phone = input("Phone number: ")
        email = input("Email: ")
        content = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nEND:VCARD"
    else:
        print("Invalid choice! Exiting the program.")
        return

    filename = input("Enter the filename to save the QR code (e.g., qrcode.png): ")

    # Create QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1-40); 1 is a 21x21 matrix
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Width of the border (in boxes)
    )
    qr.add_data(content)
    qr.make(fit=True)

    # Generate QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code
    try:
        img.save(filename)
        print(f"QR code successfully saved as {filename}!")
    except Exception as e:
        print(f"Failed to save QR code: {e}")

if __name__ == "__main__":
    generate_qr_code()
