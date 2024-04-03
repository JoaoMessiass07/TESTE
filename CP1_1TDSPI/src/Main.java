import models.Caminhao;
import models.Carro;

import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Sistema Iniciando!");

        Menu();

        System.out.println("Sistema Finalizado!");
    }

    public static Carro cadastrarCarro(){
        var carro = new Carro();
        System.out.println("Digite a marca do carro: ");
        carro.setMarca(scanner.nextLine()); // set é semelhante ao =, mas é um método
        System.out.println("Digite o modelo do carro: ");
        carro.setModelo(scanner.nextLine());
        System.out.println("Digite o ano do carro: ");
        carro.setAno(scanner.nextInt());
        scanner.nextLine();
        System.out.println("Digite o consumo do carro: ");
        carro.setConsumoPorKm(scanner.nextDouble());
        scanner.nextLine();
        return carro;
    }

    public static void Menu(){
        var carro = new Carro();
        System.out.println("Bem vindo ao sistema de controle do carro!");

        while (true) {
            System.out.println("Digite a opção desejada: ");
            System.out.println("1 - Cadastrar models.Carro");
            System.out.println("2 - Cadastrar caminhão");
            System.out.println("3 - Abastecer models.Carro");
            System.out.println("4 - Dirigir models.Carro");
            System.out.println("5 - Previsão de autonomia");
            System.out.println("6 - Sair");
            int opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {
                case 1 -> carro = cadastrarCarro();
                case 2 -> {
                    System.out.println("Digite a quantidade de litros para abastecer: ");
                    double litros = scanner.nextDouble();
                    scanner.nextLine();
                    carro.abastecer(litros);
                }
                case 3 -> {
                    System.out.println("Digite a distância a ser percorrida: ");
                    double distancia = scanner.nextDouble();
                    scanner.nextLine();
                    carro.dirigir(distancia);
                }
                case 4 ->
                        System.out.println("A previsão de autonomia do carro é de: " + carro.previsaoDeAutonomia() + "Km");
                case 5 -> {
                    System.out.println("Saindo do sistema...");
                    System.exit(0);
                }
                default -> System.out.println("Opção inválida!");
            }
        }
    }
}