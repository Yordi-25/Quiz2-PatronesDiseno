package com.company;

public class Verifier {
    public static boolean verifySequence(String userAddress){
        if (TipoDato.verify(userAddress)==false){
            // en caso de no superar esta verifición ejecutar X
            return false;
        }
        else if(LagoMinimo.verify(userAddress)==false){
            // en caso de no superar esta verifición ejecutar Y
            return false;
        }
        else if(NumerosMinimos.verify(userAddress)==false){
            // en caso de no superar esta verifición ejecutar Z
            return false;
        }
        else
            return true;
    }
}
