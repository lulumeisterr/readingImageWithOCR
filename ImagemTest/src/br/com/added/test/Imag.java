package br.com.added.test;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import net.sourceforge.tess4j.ITesseract;
import net.sourceforge.tess4j.Tesseract;
import net.sourceforge.tess4j.TesseractException;


public class Imag {


	public static void main(String[] args) throws IOException {

		FileWriter arquivo;

		File imageFile = new File("imagens/biot.jpg");

		ITesseract instance = new Tesseract();  

		instance.setDatapath("tessdata-master/tesseract-ocr");
		instance.setLanguage("por");

		try {

			String result = instance.doOCR(imageFile);
			String textoQueSeraEscrito = result;

			arquivo = new FileWriter(new File("Arquivo.txt"));
			arquivo.write(textoQueSeraEscrito);
			arquivo.close();

			System.out.println(result);

		} catch (TesseractException e) {
			System.err.println(e.getMessage());
		}

	}

}
