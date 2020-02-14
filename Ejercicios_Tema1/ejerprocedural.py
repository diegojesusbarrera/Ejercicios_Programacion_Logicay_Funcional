print ("Ejercicio Procedural");
print ("Calculadora de Areas");
var = int (input ("Seleccione una operacion a realizar" '\n'
    +  "1.- Area Cuadrado"'\n'
    +  "2.- Area Triangulo"'\n'
    +  "3.- Area Rectangulo" + '\n'
    +   "-------------- " + '\n' ));

if var is 1:
    print ("Area Cuadrado");
    a = int (input ("Digite la base " + '\n'));
    b = int (input ("Digite el altura" + '\n'));

    print ("El area del cuadrado es: " + str(a*b));

elif var is 2:
    print ("Area Triangulo");
    a = int (input ("Digite la base del triangulo " + '\n'));
    b = int (input ("Digite la altura del triangulo" + '\n'));

    print ("El area del triangulo es " + str(a*b/2));
if var is 3:
    print ("Area Rectangulo");
    a = int (input ("Digite la base " + '\n'));
    b = int (input ("Digite el altura" + '\n'));

    print ("El area del rectangulo es: " + str(a*b));
else:
    print ("No ha seleecionado ninguna operacion");

