/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package poo;
import java.util.Scanner;
/**
 *
 * @author Diego Barera
 */
public class POO {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        AutoMovil carrito=new AutoMovil();
        Scanner tecla=new Scanner(System.in);
        int km;
        carrito.arrancar();
        System.out.print("Cuantos kilometros maneja :");
        km =tecla.nextInt();
        carrito.acelelar(km);
        carrito.frenar();
    }
    
}
