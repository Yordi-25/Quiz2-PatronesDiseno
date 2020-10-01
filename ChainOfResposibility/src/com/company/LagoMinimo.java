package com.company;

public abstract class LagoMinimo implements Handler{

    public static boolean verify(String userAddress) {
        int length = userAddress.length();
        if (length < 8){
            System.out.println("La contraseña debe tener al menos 8 caracteres");
            return false;
        }else
            return true;
    }
}
