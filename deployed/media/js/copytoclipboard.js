function copyToClipboard(text) {

// ask for permission to access clipboard

try {
	netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
} catch(e) {
	alert("Kopieren in die Zwischenablage nicht erlaubt. In Firefox muss unter about:config der Wert signed.applets.codebase_principal_support auf 'true' gesetzt sein.");
	return false;
}

// make a copy of the Unicode

var str = Components.classes["@mozilla.org/supports-string;1"].createInstance(Components.interfaces.nsISupportsString);
if (!str) return false; // couldn't get string obj
str.data = text; // unicode string?


// add Unicode & HTML flavors to the transferable widget

var trans = Components.classes["@mozilla.org/widget/transferable;1"].createInstance(Components.interfaces.nsITransferable);
if (!trans) return false; //no transferable widget found

trans.addDataFlavor("text/unicode");
trans.setTransferData("text/unicode", str, text.length * 2); // *2 because it's unicode	


// copy the transferable widget!

var clipboard = Components.classes["@mozilla.org/widget/clipboard;1"].getService(Components.interfaces.nsIClipboard);
if (!clipboard) return false; // couldn't get the clipboard

clipboard.setData(trans, null, Components.interfaces.nsIClipboard.kGlobalClipboard);
return true;

}
