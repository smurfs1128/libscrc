![](https://github.com/hex-in/libscrc/workflows/Python%20package/badge.svg)

libscrc
=======
libscrc is a library for calculating CRC4 CRC5 CRC6 CRC7 CRC8 CRC16 CRC32 CRC64.

|  CRCx |  CRC8 | CRC16  |   CRC32| CRC64  |
| :------------: | :------------: | :------------: | :------------: | :------------: |
| CRC4-ITU | INTEL   | MODBUS   | FSC      | ISO    |
| CRC5-ITU | BCC     | IBM      | CRC32    | ECMA182|
| CRC5-EPC | LRC     | XMODEM | MPEG2    |        |
| CRC5-USB | MAXIM8  | CCITT    |ADLER32   |        |
| CRC6-ITU | ROHC    | KERMIT   |FLETCHER32|        |
| CRC7-MMC | ITU8    |MCRF4XX   |          |        |
|          | CRC8    | SICK     |          |        |
|          | SUM8    | DNP      |          |        |
|          |FLETCHER8| X25      |          |        |
|          |         | USB      |          |        |
|          |         | MAXIM16  |          |        |
|          |         | DECT     |          |        |
|          |         | TCP      |          |        |
|          |         | UDP      |          |        |
|          |         |FLETCHER16|          |        |


Installation
------------

1. Compile and install the library

```
#pip3 install libscrc
```

​     or

```
#python3 setup.py build
#python3 setup.py install
```

You will need the administrative privileges to execute the last command.

2. After installation you can run unit tests to make sure that the library works fine.  Execute

```
#python3 -m libscrc.test.modbus
#python3 -m libscrc.test.crc64
```




Usage
-----

  In Python 3

```python
import libscrc
crc16 = libscrc.modbus(b'1234')      # Calculate ASCII of modbus
crc16 = libscrc.modbus(b'\x01\x02')  # Calculate HEX of modbus
```

  You can also calculate CRC gradually

```python
import libscrc
crc16 = libscrc.xmodem(b'1234')
crc16 = libscrc.xmodem(b'5678', crc16)
```

Example
-------
1. CRCx

```python
crc4 = libscrc.itu4(b'1234')
crc5 = libscrc.itu5(b'1234')
crc5 = libscrc.epc(b'1234')
crc5 = libscrc.usb5(b'1234')
crc6 = libscrc.itu6(b'1234')
crc7 = libscrc.mmc(b'1234')
```

2. CRC8

```python
crc8 = libscrc.intel(b'1234')
crc8 = libscrc.bcc(b'1234')  
crc8 = libscrc.lrc(b'1234')  
crc8 = libscrc.maxim8(b'1234')
crc8 = libscrc.rohc(b'1234')
crc8 = libscrc.itu8(b'1234')
crc8 = libscrc.crc8(b'1234')
```

3. CRC16

```python
crc16 = libscrc.ibm(b'1234')            # poly=0xA001 (default Reversed)
crc16 = libscrc.ibm(b'1234', 0x8005)    # poly=0x8005 (Normal)
crc16 = libscrc.modbus(b'1234')
crc16 = libscrc.xmodem(b'1234')
crc16 = libscrc.ccitt(b'1234')
crc16 = libscrc.ccitt_false(b'1234')
crc16 = libscrc.kermit(b'1234')
crc16 = libscrc.mcrf4xx(b'1234')
crc16 = libscrc.sick(b'1234')
crc16 = libscrc.mcrf4xx(b'1234')
crc16 = libscrc.dnp(b'1234')
crc16 = libscrc.x25(b'1234')
crc16 = libscrc.usb16(b'1234')
crc16 = libscrc.maxim16(b'1234')
crc16 = libscrc.dect(b'1234')           # poly=0x0589 (Cordless Telephones)

data  = b'\x45\x00\x00\x3c\x00\x00\x00\x00\x40\x11\x00\x00\xc0\xa8\x2b\xc3\x08\x08\x08\x08\x11'
crc16 = libscrc.tcp( data )             # 13933
crc16 = libscrc.udp( data )             # 13933

# init=0xFFFF(default)
# xorout=0x0000(default)

crc16 = libscrc.hacker16( b'123456789', poly=0xA001 )
crc16 = libscrc.hacker16( b'123456789', poly=0xA001, init=0, xorout=0xFFFF )
```

4. CRC32

```python
crc32 = libscrc.fsc(b'1234')            # Ethernet frame sequence (FSC)
crc32 = libscrc.mpeg2(b'1234')          # MPEG2
crc32 = libscrc.crc32(b'1234')          # WinRAR, File

# init=0xFFFFFFFF(default)
# xorout=0x00000000(default)
crc32 = libscrc.hacker32( b'123456789', poly=0x04C11DB7 )
crc32 = libscrc.hacker32( b'123456789', poly=0x04C11DB7, init=0, xorout=0xFFFFFFFF )
```

5. CRC64

```python
crc64 = libscrc.iso(b'1234')
crc64 = libscrc.ecma182(b'1234')

# init=0xFFFFFFFFFFFFFFFF(default)
# xorout=0x0000000000000000(default)
crc64 = libscrc.hacker64( b'123456789', poly=0xD800000000000000, init=0 )
```



NOTICE
------
* v0.1.6+ version will not support python2 series (2020-01-20)

### **V1.0 (2020-03-23)**

------------
* New hacker8 \ hacker16 \ hacker32 \ hacker64
* New FLETCHER8 \ FLETCHER16 \ FLETCHER32

### **V0.1.5 (2017-09-22)**

------------
* New CRC4-ITU      Poly = 0x03 Initial = 0x00 Xorout=0x00 Refin=True Refout=True
* New CRC5-ITU      Poly = 0x15 Initial = 0x00 Xorout=0x00 Refin=True Refout=True
* New CRC5-EPC      Poly = 0x09 Initial = 0x09 Xorout=0x00 Refin=False Refout=False
* New CRC5-USB      Poly = 0x05 Initial = 0x1F Xorout=0x1F Refin=True Refout=True
* New CRC6-ITU      Poly = 0x03 Initial = 0x00 Xorout=0x00 Refin=True Refout=True
* New CRC7-MMC      Poly = 0x09 Initial = 0x00 Xorout=0x00 Refin=False Refout=False

### **V0.1.4 (2017-09-21)**

------------
* New CRC8-MAXIM8   Poly = 0x31 Initial = 0x00 Xorout=0x00 Refin=True  Refout=True
* New CRC8-ROHC     Poly = 0x07 Initial = 0xFF Xorout=0x00 Refin=True  Refout=True
* New CRC8-ITU      Poly = 0x07 Initial = 0x00 Xorout=0x55 Refin=False Refout=False
* New CRC8-CRC8     Poly = 0x07 Initial = 0x00 Xorout=0x00 Refin=False Refout=False

### **V0.1.3 (2017-09-19)**

------------
* New CRC16-X25  
* New CRC16-USB  
* New CRC16-MAXIM16  
* New CRC16-CCITT_FALSE
* New CRC16-DECT

Bugfixes
  * Calculate CRC16-IBM of poly = 0x8005 is ERROR.

### **V0.1.2 (2017-08-22)**

------------

Platform Support
  * Win32
  * Linux_x86_64
  * MacOSX_10_6_intel
  * ARMv7 (Toradex Ixora iMX6 Linux-4.1.41)

Bugfixes
  * Coding C99 standard.
  * Python/C API parsing arguments type error in linux.

### **V0.1.1 (2017-08-20)**

------------
* New CRC16-NDP and CRC16-SICK

