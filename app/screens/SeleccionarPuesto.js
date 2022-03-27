import React from 'react';
import { StyleSheet, View, Butto, Text } from 'react-native';

function SeleccionarPuesto(props) {
    return (
        <View style={styles.background}>
            <View >
                <Text>Header</Text>
            </View>
            <View >
                <Text>Input</Text>
            </View>
            <View >
                <Text>Botones</Text>
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    background: {
        flex: 1,
        backgroundColor: "#F2F2F2",
        alignItems: 'center',
    },
})

export default SeleccionarPuesto;