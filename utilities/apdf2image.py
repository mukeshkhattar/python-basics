import locale
import tempfile
import ghostscript


from google.cloud import storage

storage_client = storage.Client()

def convert_pdf(event, context):
    storage_client = storage.Client()
    bucket_name = event['bucket']
    pdf = event['name']
    if pdf.startswith('v-'):
        return
    print('starting convertingg..')
    blob = storage_client.bucket(bucket_name).get_blob(pdf)

    _, tmp_pdf = tempfile.mkstemp()
    _, tmp_png = tempfile.mkstemp()

    tmp_png = tmp_png+".png"

    blob.download_to_filename(tmp_pdf)
    print('download success')

    # create a temp folder based on temp_local_filename
    # use ghostscript to export the pdf into pages as pngs in the temp dir
    args = [
        "pdf2png", # actual value doesn't matter
        "-dSAFER",
        "-sDEVICE=pngalpha",
        "-o", tmp_png,
        "-r300", tmp_pdf
        ]
    print('export success')
    # the above arguments have to be bytes, encode them
    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]
    #run the request through ghostscript
    ghostscript.Ghostscript(*args)

    print("Image created")
    new_file_name = "v-"+pdf.split('.')[0]+".png"
    blob.bucket.blob(new_file_name).upload_from_filename(tmp_png)

'''
import os
import tempfile

from google.cloud import storage
from wand.image import Image

storage_client = storage.Client()

def convert_pdf(event, context):

    storage_client = storage.Client()
    bucket_name = event['bucket']
    file_name = event['name']
    current_blob = storage_client.bucket(bucket_name).get_blob(file_name)
    # Ignore image files
    if not (file_name.endswith('.pdf') or file_name.endswith('.PDF')):
        print(f'The file {file_name} is not pdf')
        return
    # Process image
    file_name = current_blob.name
    _, temp_local_filename = tempfile.mkstemp()

    # Download file from bucket.
    current_blob.download_to_filename(temp_local_filename)
    print(f'File {file_name} was downloaded to {temp_local_filename}.')

    # Convert the PDF using ImageMagick.
    with Image(filename=temp_local_filename) as image:
      print('pages = ', len(img.sequence))

      with image.convert('png') as converted:
        converted.save(filename='test.png')

    print(f'PDF {file_name} was converted.')

    # Upload result to a second bucket, to avoid re-triggering the function.
    # You could instead re-upload it to the same bucket + tell your function
    # to ignore files marked as blurred (e.g. those with a "blurred" prefix)
    image_bucket = storage_client.bucket(bucket_name)
    new_blob = image_bucket.blob('test.png')
    new_blob.upload_from_filename('test.png')
    print(f' image uploaded to: gs://{image_bucket}')

    # Delete the temporary file.
    os.remove(temp_local_filename)

'''
