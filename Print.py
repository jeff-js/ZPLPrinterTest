from optparse import OptionParser

if __name__ == "__main__":

    parser = OptionParser(usage="usage: %prog [options]", version="%prog 1.0")
    parser.add_option("--firstName", default='echo', type='string', action="store", dest="firstName", help="echo, chat")
    parser.add_option("--lastName", default='echo', type='string', action="store", dest="lastName", help="echo, chat")
    parser.add_option("--company", default='echo', type='string', action="store", dest="company", help="echo, chat")
    parser.add_option("--assistentType", default='echo', type='string', action="store", dest="assistentType", help="echo, chat")
    parser.add_option("--assistentId", default='echo', type='string', action="store", dest="assistentId", help="echo, chat")
    parser.add_option("--printer", default='echo', type='string', action="store", dest="printer", help="echo, chat")

    (options, args) = parser.parse_args()
    print(options)
    nombreAsistente = str.upper(options.firstName)
    apellidoAsistente = str.upper(options.lastName)
    empresa = str.upper(options.company)
    tipoVisitante = str.upper(options.assistentType)
    asistenteId = options.assistentId
    label = """
    ^XA
    ^FO100, 30
    ^A0,65,40^FH
    ^FD"""+nombreAsistente+"""^FS
    ^FO100, 90
    ^A0,65,40^FH
    ^FD"""+apellidoAsistente+"""^FS
    ^FO100, 160
    ^A0,40,25^FH
    ^FD"""+empresa+"""^FS
    ^FO100, 240
    ^A0,40,25^FH
    ^FD"""+tipoVisitante+"""^FS
    ^FO600,220
    ^BQN,2,5
    ^FDMA,"""+asistenteId+"""^FS
    ^XZ
    """
    #print(label)
    from zebra import zebra
    z = zebra(options.printer)
    z.output(label)
    #python3 Print.py --firstName=Jefferson --lastName=Aguilar --company=alun ideas --assistentType=vip --assistentId=asdasdasdasdasdasdas