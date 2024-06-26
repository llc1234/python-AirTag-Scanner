import simplepyble


data_client = []

APPLE_MAN_ID = "0x4C"
FINDMY_DATA = bytes([0x12, 0x19])
AIR_TAG_STATUSES = bytes([0x10, 0x50, 0x90, 0xd0])

adapter = simplepyble.Adapter.get_adapters()[0]

while True:
    adapter.scan_for(2000)

    for peripheral in adapter.scan_get_results():
        manufacturer_data = peripheral.manufacturer_data()
        for manufacturer_id, value in manufacturer_data.items():
            if manufacturer_id == int(APPLE_MAN_ID, 16):
                if value.startswith(FINDMY_DATA):
                    status_byte = value[2:3]
                    if status_byte in AIR_TAG_STATUSES:
                        rssi = peripheral.rssi()
                        byte = value.hex().upper()

                        i_n = False
                        for pp in data_client:
                            if pp["bytes"] == byte:
                                i_n = True

                        if not i_n:
                            data_client.append({"bytes": byte, "name": "the_name"})
                            print(f"{byte} - Found AirTag, rssi: {rssi}")
