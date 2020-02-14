
package poo;

/**
 *
 * @author Diego Barrera
 */
public class AutoMovil {
static private String color, marca, modelo; 
static private int caballosMotor;


void arrancar(){
    System.out.println("Nos Fuimos!");   
}

void acelelar(int km){
    System.out.println("Vamos a:"+km+"km por hora");   
}

void frenar(){
    System.out.println("Me Detuve!");   
}
}
