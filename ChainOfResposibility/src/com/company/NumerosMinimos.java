package com.company;

public abstract class NumerosMinimos implements Handler{

    public static boolean verify(String userAddress) {
        int cont = 0;
        char[] chars = userAddress.toCharArray();
        for (char c: chars) {
            System.out.println(Character.isDigit(c));
            if (Character.isDigit(c))
                cont++;
        }
        if (cont < 4) {
            System.out.println("La contraseña debe tener al menos 4 caracteres numéricos");
            return false;
        } else
            return true;


    }
}
