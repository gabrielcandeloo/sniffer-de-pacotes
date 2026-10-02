from scapy.all import sniff, dev_from_index

print("\n--- INICIANDO CAPTURA EXCLUSIVA TCP ---") # <- Adicione esta linha!

minha_placa = dev_from_index(6)

pacostes_capturados = sniff(count=10, filter="tcp", iface=minha_placa)

for pacote in pacostes_capturados:
    print(pacote.summary())