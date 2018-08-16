package br.com.added.test;

import java.io.File;
import net.sourceforge.tess4j.*;

public class Imag {
	
	
	public static void main(String[] args) {
		
		File imageFile = new File("imagens/exame.jpg");
	    ITesseract instance = new Tesseract();  
	    instance.setDatapath("/ImagemTest/tessdata-master");
	    instance.setLanguage("por.traineddata");
	    
	    try {
	        String result = instance.doOCR(imageFile);
	        System.out.println(result);
	    } catch (TesseractException e) {
	        System.err.println(e.getMessage());
	    }
	    
		
	}

}
