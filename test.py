from rembg import remove

input_path = "bg.png"
output_path = "bg-r.png"

with open(input_path, "rb") as i:
    with open(input_path, "wb") as o:
        input = i.read()
        output = remove(input)
        o.write(output)
