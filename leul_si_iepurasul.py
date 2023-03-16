print("Viteza iepurelui :")
v_iepure = int(input())
print("Viteza leului :")
v_leu = int(input())
print("Timpul dupa care leul pleaca : ")
t_aparitie = int(input())
if v_leu <= v_iepure:
    print("Leul nu prinde iepurele.")
    print(-1)
else:
    print(f"Leul prinde iepurele dupa {v_iepure * t_aparitie / (v_leu - v_iepure)}")
    
