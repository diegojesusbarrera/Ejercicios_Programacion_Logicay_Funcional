es_un_sintoma(pitidos cortos continuos).
es_un_sintoma(un_pitido_largo_y_dos_cortos).
es_un_sintoma(dos_pitidos__largos_y_una_corto).
es_un_sintoma(seis_pitidos_cortos).
sintoma_de(pitidos_cortos_continuos,placa_base_esta_defectuosa_o_deteriorada).
sintoma_de(dos_pitidos__largos_y_una_corto,error_en_la_sincronizacion_de_las_
imagenes).
sintoma_de(seis_pitidos_cortos,error_en_el_teclado).
problema_de(x,y):-es_un_sintoma(x),sintoma_de(x,y).
