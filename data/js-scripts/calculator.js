var Operation = { MINUS : 1, PLUS : 2, DIV : 3, TIMES : 4, NUMBER : 5 };
var TreeElem = function() {

    this.type = Operation.NUMBER;
    this.value = 0;
    
    this.left = null;
    this.right = null;
}
TreeElem.prototype.addElem = function ( tree, elem ) {

    if ( tree == null ) {
        
        tree = elem;
    }
    else {
    
        if ( elem.type <= tree.type ) {
        
            var auxTree = tree;
            tree = elem;
            elem.left = auxTree;
        }
        else {
        
            tree.right = TreeElem.prototype.addElem ( tree.right, elem );
        }
    }
    
    return tree;
}

var buildTreeExpression = function ( text ) {
		
    var tree = null;
    
    var lastChar = text[ text.length - 1 ];
    if ( isNaN( lastChar ) ) {
        // removing the last char 
        text = text.substring( 0, text.length - 1 );
    }
    
    var numberStr = '';
    for ( var i = 0; i < text.length; i++ ) {
    
        var currChar = text[ i ];
        if ( !isNaN( currChar ) || currChar == '.' 
            || numberStr == '' && currChar == '-' ) 
        {
            numberStr += currChar;
        }
        else {
        
            // add number to tree
            var number = new TreeElem();
            number.value = numberStr;
            numberStr = ''; // cleaning up this variable
            
            tree = TreeElem.prototype.addElem ( tree, number );
            
            // add operation to tree
            var operation = new TreeElem();
            switch ( currChar ) {
                
                case '-' : operation.type = Operation.MINUS; break;
                case '+' : operation.type = Operation.PLUS; break;
                case '/' : operation.type = Operation.DIV; break;
                case '*' : operation.type = Operation.TIMES; break;
            }
            
            tree = TreeElem.prototype.addElem ( tree, operation );
        }
    }
    
    // add last number
    var lastNumber = new TreeElem();
    lastNumber.value = numberStr;
    tree = TreeElem.prototype.addElem ( tree, lastNumber );
    
    return tree;
}

// doesn't work with ES6 at least yet
//var calc = ( tree ) => {
var calc = function( tree ) {    
		
    if ( tree.left == null && tree.right == null ) {
        
        return Number(tree.value);
    }
    else {
    
        var subResult = 0;
        
        switch ( tree.type ) {
        
            case Operation.MINUS : 
                subResult = calc( tree.left ) - calc( tree.right ); break;
            case Operation.PLUS : 
                subResult = calc( tree.left ) + calc( tree.right ); break;
            case Operation.DIV : 
                subResult = calc( tree.left ) / calc( tree.right ); break;
            case Operation.TIMES : 
                subResult = calc( tree.left ) * calc( tree.right ); break;						
        }
        
        return subResult;
    }
}

var calculate = function(str) {
    tree = buildTreeExpression(str)
    return calc(tree)
}