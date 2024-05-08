package beans;

public class Debito extends Cartao{
    private double consignado;

    public Debito(String banco, String bandeira, String nome, String cor, int numero, int cvv, double saldo, double compra) {
        super(banco, bandeira, nome, cor, numero, cvv, saldo, compra);
    }
}
