Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre. Numărul globuleţelor
albe se citeşte de la tastatură. Câte globuleţe are brăduţul, ştiind că numărul de
globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, iar globuleţele
albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii. Exemplu: Date de intrare:
12 Date de ieşire: 52.


na=int(input("dati numarul de globuri albe"))
nr= na + 3
nb= (na + nr) - 2
nt= nr + nb + na
print("Pe brad sunt globulete",nt)
