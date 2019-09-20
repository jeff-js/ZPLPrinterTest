nombreAsistente = str.upper("jefferson")
apellidoAsistente = str.upper("aguilar")
empresa = str.upper("alunideas")
tipoVisitante = str.upper("vip")
asistenteId = "d090621a-380e-42fd-9d0f-681d27d94d48"
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
from zebra import zebra
z = zebra("GT800_04")
z.output(label)
