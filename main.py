import os
import socket
import dpkt
import pygeoip

gi = pygeoip.GeoIP("GeoLiteCity.dat")

def retKML(dstip, srcip):
    dst = gi.record_by_name(dstip)
    src = gi.record_by_name('x.xxx.xxx.xxx')  # Use actual srcip here
    try:
        dstlon = dst['longitude']
        dstlat = dst['latitude']
        srclon = src['longitude']
        srclat = src['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        ) % (dstip, dstlon, dstlat, srclon, srclat)
        return kml
    except TypeError:
        # Handle case where GeoIP record is not found
        return ''

def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if isinstance(ip, dpkt.ip.IP):
                src = socket.inet_ntoa(ip.src)
                dst = socket.inet_ntoa(ip.dst)
                KML = retKML(dst, src)
                kmlPts += KML
        except Exception as e:
            print(f"Error processing packet: {e}")
            pass
    return kmlPts

def main():
    with open("dump.pcap", "rb") as f:
        pcap = dpkt.pcap.Reader(f)
        kmlheader = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'
            '<Style id="transBluePoly">\n'
            '<LineStyle>\n'
            '<width>1.5</width>\n'
            '<color>501400FF</color>\n'
            '</LineStyle>\n'
            '</Style>\n'
        )
        kmlfooter = '</Document>\n</kml>\n'
        kmldoc = kmlheader + plotIPs(pcap) + kmlfooter

        with open("myplaces.kml", "w") as file:
            file.write(kmldoc)

if __name__ == "__main__":
    main()
