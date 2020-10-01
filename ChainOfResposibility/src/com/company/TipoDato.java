package com.company;

public abstract class TipoDato implements Handler{


//    @Override
    public static boolean verify(String userAddress) {
        if (userAddress instanceof String) {
            return true;
        }
        else
            return false;

    }
}
