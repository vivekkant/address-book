import vobject

def get_vcards(filename):
    """
        Returns list of vCard object by reading a file
    """
    vcards = []
    with open(filename) as source:
        for vcard in vobject.readComponents(source):
            vcards.append(vcard)

    return vcards

vcards = get_vcards("/Users/vivekkant/temp/vcard/iphone-contacts-22-09-01.vcf")
for vcard in vcards:
    print(vcard.fn.value)
print("Total: ", len(vcards))