import { StyleSheet } from "react-native";

const style = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent:"center"
    },
    iconeAlerta:{
        width:48, 
        height:48,
        position: "absolute",
        bottom: 75,
        right: 13,
        zIndex: 999
    },
        modalContainer: {
          flex: 1,
          justifyContent: 'center',
          alignItems: 'center',
          backgroundColor: 'rgba(0, 0, 0, 0.5)',
        },
        modalContent: {
          backgroundColor: 'white',
          borderRadius: 10,
        },
        imagem: {
          width: 25,
          height: 25,
          marginBottom: 10,
        },
        flexAlerta:{
            flexDirection: "row",
            gap: 10
        },
        button:{   
            justifyContent: "center",
            alignItems: "center",
            width: '35%',
            height: 110,
        },
    
        fundo_acidente:{
            backgroundColor: "#ff6868",
            padding: 5, 
            borderRadius: 60
        },
    
        fundo_eletricidade:{
            backgroundColor: "#ffdd70",
            padding:5, 
            borderRadius: 60
        },
    
        fundo_movimento:{
            backgroundColor: "#6295f1",
            padding:5, 
            borderRadius: 60
        },
    
        fundo_obras:{
            backgroundColor: "#ff9a61",
            padding:5, 
            borderRadius: 60
        },
    
        fundo_lentidao:{
            backgroundColor: "#ffdd70",
            padding:5, 
            borderRadius: 60
        },
    
        fundo_sos:{
            backgroundColor: "#ff003d",
            padding:5, 
            borderRadius: 60
        },
    
        imageAlerta: {
            width: 60,
            height: 60, 
        },
    
        txtAlerta:{
            paddingTop: 6,
            fontWeight: "600",
            fontSize: 15,
        },
    
        txtAlertaSOS:{
            paddingTop: 6,
            fontWeight: "600",
            fontSize: 15,
            fontWeight: "bold"
        },
    
        atualizacoes:{
            width: '80%',
        },
    
        txtAtualizacoes:{
            marginTop: '10%',
            textAlign: "center",
            fontWeight: "300"
        },



      });

export default style;