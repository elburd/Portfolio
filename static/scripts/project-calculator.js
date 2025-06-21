const screenElement = document.getElementById('screen');

function formatValue(value) {
	const validChars = new Set([
		'0', '1', '2', 
		'3', '4', '5',
		'6', '7', '8',
		'9', '+', '-',
		'*', '/', '(',
		')', '.',
		]	
	)
	let valueString = '';
	for (let i = 0; i < value.length ; i++) {
		if (validChars.has(value[i])) {
			valueString += value[i];
		}
		else if (value[i] === 'x') {
			// The eval() function does not recognize 'x' as the symbol for multiplication, this also acts as QoL for certain users
			valueString += '*';
		}
		// else {
		// 	// Prevent invalid characters from reaching the eval() function in calculateResult()
		// 	return false;
		// }
	}
	return valueString;
}

function calculateResult(value) {
	const formattedValue = formatValue(value);
	const result = eval(formattedValue);
	return result;
}

function showResult() {
	const inputValue = screenElement.value;
	const result = inputValue && calculateResult(inputValue);
	if (typeof result === 'number') {
		screenElement.value = result;
	}
}

function pushValue(character) {
	screenElement.value += character;
}

function resetValue() {
	screenElement.value = '';
}

function backspace() {
	screenElement.value = screenElement.value.slice(0, -1);
}