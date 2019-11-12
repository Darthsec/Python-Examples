seg_converter = input("Por favor, entre com o numero de seg: ")
total_seg = int(seg_converter)

dias = (total_seg // 3600) // 24
horas = (total_seg // 3600) % 24
segs_restantes = total_seg % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos." )
