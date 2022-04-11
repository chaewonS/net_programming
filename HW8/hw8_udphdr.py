import socket
import struct
import binascii

#Udphdr 클래스 정의
class UdpHeader:
    def __init__(self, sport, dport, length, checksum):
        self.sport = sport
        self.dport = dport
        self.length = length
        self.checksum = checksum

    #pack_Udphdr() 함수 정의
    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!4H', self.sport, self.dport, self.length, self.checksum)
        return packed

    #unpack_Udphdr() 함수 정의
    def unpack_Udphdr(buffer):
        unpacked = struct.unpack('!4H', buffer[:20])
        return unpacked

    #unpack된 결과에서 해당하는 필드값을 가져오는 함수(4개)
    def getSrcPort(unpacked):
        return unpacked[0]

    def getDstPort(unpacked):
        return unpacked[1]

    def getLength(unpacked):
        return unpacked[2]

    def getChecksum(unpacked):
        return unpacked[3]

#UDP 헤더 생성
udp = UdpHeader(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = UdpHeader.unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)

print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'
        .format(UdpHeader.getSrcPort(unpacked_udphdr),UdpHeader.getDstPort(unpacked_udphdr),UdpHeader.getLength(unpacked_udphdr),UdpHeader.getChecksum(unpacked_udphdr)))