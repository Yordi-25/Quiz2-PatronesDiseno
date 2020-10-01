package com.company;

import java.util.Scanner;

public class Main {
    static String userAddress;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean nuevaContraseña = true;
        while (nuevaContraseña) {
            System.out.println("Ingrese su contraseña nueva");
            userAddress = scanner.nextLine();
            if (Verifier.verifySequence(userAddress) == true){
                System.out.println("Su contraseña ha sido cambiada");
                nuevaContraseña = false;
            }else
                nuevaContraseña = true;

        }
    }
}
