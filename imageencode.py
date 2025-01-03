from PIL import Image
import sys

import rs

rowstride = 255

def encode(input, output_filename):
    """Encodes the input data with reed-solomon error correction in 223 byte
    blocks, and outputs each block along with 32 parity bytes to a new file by
    the given filename.

    input is a file-like object

    The outputted image will be in png format, and will be 255 by x pixels with
    one color channel. X is the number of 255 byte blocks from the input. Each
    block of data will be one row, therefore, the data can be recovered if no
    more than 16 pixels per row are altered.
    """
    coder = rs.RSCoder(255,223)

    output = []
    with open(input, mode='rb') as file:
        block = file.read(223)
        while block:
            # print(block)
            code = coder.encode(block)
            # print(':'.join(x.encode('hex') for x in code))
            output.append(code)
            print(len(output))
            # b is important -> binary
            block = file.read(223)
            sys.stderr.write(".")

    sys.stderr.write("\n")
    # with open("test.bin", "wb") as file:
    #     file.write(code.encode('binary'))
    out = Image.new("L", (rowstride,len(output)))
    out.putdata("".join(output))
    out.save(output_filename)

def decode(input_filename):
    coder = rs.RSCoder(255,223)
    input = Image.open(input_filename)
    data = "".join(chr(x) for x in input.getdata())
    del input

    blocknum = 0
    while True:
        if blocknum*255 > len(data):
            break
        rowdata = data[blocknum*255:(blocknum+1)*255]

        decoded = coder.decode(rowdata)

        blocknum += 1
        sys.stdout.write(str(decoded))
        # sys.stderr.write(".\n")
    sys.stderr.write("\n")

if __name__ == "__main__":
    # if "-d" == sys.argv[1]:
    #     # decode
    #     decode(sys.argv[2])

    # else:
        # encode
        # encode(sys.stdin,sys.argv[1])
        # message = "This is a secret Message!"
        # print("Encoding Message: ",message)
        # encode(sys.argv[1], sys.argv[1])
        # encode("message.txt", "message_enc.png")
    message = "message"
    # message = "alice_wonderland"
    message_file = message + ".txt"
    output_file = message+"_enc"+".png"
    if "-e" == sys.argv[1]:
        encode(message_file, output_file)
    if "-d" == sys.argv[1]:
        decode(output_file)

    # encode("4CmAn.png", "4CmAn_enc.png")
