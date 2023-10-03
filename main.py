import xml.etree.ElementTree as ET

# Load the XLIFF file
tree = ET.parse('/Users/takasurazeem/Desktop/QuranMajeed Localizations/ur.xliff')
root = tree.getroot()

# Define namespaces used in the XLIFF file
namespaces = {
    'xliff': 'urn:oasis:names:tc:xliff:document:1.2',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
}

# Find all trans-unit elements within the XLIFF file
trans_units = root.findall('.//xliff:trans-unit', namespaces)

# Iterate through the trans-unit elements and extract information
for trans_unit in trans_units:
    unit_id = trans_unit.get('id')
    source = trans_unit.find('./xliff:source', namespaces).text

    # Check if a note element exists within the trans-unit
    note = trans_unit.find('./xliff:note', namespaces)
    if note is not None:
        note_text = note.text
    else:
        note_text = None

    # Check if a target element exists within the trans-unit
    target = trans_unit.find('./xliff:target', namespaces)
    if target is not None:
        target_text = target.text
        target_state = target.get('state')
    else:
        target_text = None
        target_state = None

    print(f"ID: {unit_id}")
    print(f"Source: {source}")
    print(f"Note: {note_text}")
    print(f"Target: {target_text}")
    print(f"Target State: {target_state}")
    print()
