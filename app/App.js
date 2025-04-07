import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, TextInput, Pressable } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <View> {/* Container Image */}
        <Image source={{ uri: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png" }}
          width={200}
          height={200} />
      </View>
      <View>
        <Text style={styles.title}>Iniciar Sesion</Text> {/* title */}
        <Text style={styles.lable} >Correo: </Text> {/* lable */}
        <TextInput style={styles.input} />
        <Text style={styles.lable}>Contraseña:</Text> {/* lable */}
        <TextInput style={styles.input} />
        <Pressable style={styles.send} title='Enviar'>
          <Text style={styles.send.textButton}>Enviar</Text>
        </Pressable>
      </View>
      <View style={styles.containerFooter}> {/* container-footer */}
        <Text style={styles.containerFooter.texts}>¿Olvidaste tu Contraseña?</Text>
        <Text style={styles.containerFooter.texts}>Registrate</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: .5,
    backgroundColor: '#fff',
    padding: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 34,
    fontWeight: "bold",
  },
  lable: {
    fontSize: 20,
    fontWeight: "bold",
  },
  input: {
    borderRadius: 10,
    borderWidth: 2,
    borderColor: "black",
    fontSize: 15,
    height: 25,
    width: 200,
    backgroundColor: "silver"
  },

  send: {
    backgroundColor: "#ff3b19",
    width: "auto",
    height: "auto",
    fontWeight: "bold",
    borderRadius: 10,
    marginTop: 15,
    alignItems: "center",
    textButton: {
      color: "black",
      fontSize: 20,
      fontWeight: "bold"
    }
  },
  containerFooter: {
    justifyContent: "space-around",
    texts: {
      fontSize: 20,
      margin: 5,
    }
  },

  
});
