import React from 'react';
import { Image, StyleSheet, View, Button } from 'react-native';

function Bienvenida(props) {
    return (
        <View style={styles.background}>
            <View style={styles.logoContainer}>
                <Image style={styles.logo} source={require("../assets/testigos-logo.svg")}/>
                {/* <Text>Sell what you don't need</Text> */}
            </View>
            <View style={styles.startButtonContainer}>
                <Button  color = "#DE4E51" title="¿Se robaron tu voto?" onPress={() => Alert.alert('Simple')} />
            </View>

        </View>
    );
}

const styles = StyleSheet.create({
    background: {
        flex: 1,
        backgroundColor: "#FCDE67",
        alignItems: 'center',
        // flexDirection: 'row',
        // flexWrap: 'wrap',
    },
    startButtonContainer: {
        width: '90%',
        // height: 10,
        flex: 1,
        justifyContent: 'flex-end',
        marginBottom: 50,
    },
    logo: {
        width: 133,
        height: 90,
    },
    logoContainer: {
        position: 'absolute',
        top: 190,
        alignItems: "center",
    },
})

export default Bienvenida;