import zlib, base64

def compression(inputfile, outputfile):
    file = open(inputfile, "r").read()
    file_bytes = bytes(file, "utf-8")
    compressed_data = base64.b64encode(zlib.compress(file_bytes, 9))
    decoded_file = compressed_data.decode("utf-8")
    compressed_file = open(outputfile, "w")
    compressed_file.write(decoded_file)
def decompression(inputfile,outputfile):
    file_content= open(inputfile,'r').read()
    encoded_file=file_content.encode('utf-8')
    decompressed_file = zlib.decompress(base64.b64decode(encoded_file))
    decoded_file=decompressed_file.decode('utf-8')
    new_file=open(outputfile,'w')
    new_file.write(decoded_file)
    new_file.close()
