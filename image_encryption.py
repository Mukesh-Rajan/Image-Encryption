from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Convert the image to RGB mode
    img = img.convert("RGB")
    
    # Encrypting the image
    pixels = img.load()
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Example encryption operation: XOR with key
            r = r ^ key
            g = g ^ key
            b = b ^ key
            pixels[x, y] = (r, g, b)
    
    # Save the encrypted image
    encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
    img.save(encrypted_image_path)
    print("Image encrypted successfully!")
    return encrypted_image_path

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    width, height = img.size
    
    # Decrypting the image
    pixels = img.load()
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Example decryption operation: XOR with key
            r = r ^ key
            g = g ^ key
            b = b ^ key
            pixels[x, y] = (r, g, b)
    
    # Save the decrypted image
    decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'
    img.save(decrypted_image_path)
    print("Image decrypted successfully!")
    return decrypted_image_path

# Example usage:
image_path = "example_image.png"
encryption_key = 123
encrypted_image = encrypt_image(image_path, encryption_key)
decrypted_image = decrypt_image(encrypted_image, encryption_key)
