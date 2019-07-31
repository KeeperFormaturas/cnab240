from keeper_cnab240.file import File
import hashlib


def hash_file(fname, ashexstr=False):
    return hash_bytestr_iter(file_as_blockiter(open(fname, 'rb')), hashlib.sha256(), ashexstr)


def hash_bytestr_iter(bytesiter, hasher, ashexstr=False):
    for block in bytesiter:
        hasher.update(block)
    return hasher.hexdigest() if ashexstr else hasher.digest()


def file_as_blockiter(afile, blocksize=65536):
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


def payment_file_generator(bank_name, company, payments):
    payment_file = File(bank_name, company)
    payment_file.header.set_company_data(company)
    payment_file.payments = []

    for payment in payments:
        payment_file.add_payment(payment)

    payment_file.generate()
    return payment_file.get_content()
