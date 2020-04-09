 function twixt($ft,$bt,$disp,$bo) {
     if ($ft == '') { 
        $fo = 0;
     } else {
        $fo = strpos($disp,$ft,$bo);
     } // endif
     $bo1 = strpos($disp,$bt,$fo);
     if ($fo ==0 ) {
        $tok = trim(substr($disp,$fo,$bo1));
     } else {
       $tok = trim(substr($disp,$fo+strlen($ft),$bo1-$fo-strlen($ft)));
     } // endif
     return(array($fo,$bo1,$tok));
 } // end-twixt
 function logg($tx) {
     echo("[[".$tx."]]");
 } // end-logg
 
 $filename = '_customer1.html';
 $fileToOpen = fopen($filename,"r");
 $disp = fread($fileToOpen, filesize($filename));
 $bo=0;
 list($fo,$bo,$tok) = twixt('/*','*/',$disp,$bo);
 logg($tok);
 // format type-name( c=v )
 $bo1 = 0;
 list($fo1,$bo1,$tok1) = twixt('','-',$tok,$bo1);
 logg($tok1);
 $type = $tok1;
 logg($type);
 list($fo1,$bo1,$tok1) = twixt('-','(',$tok,$bo1);
 $name = $tok1;
 logg($name);
 list($fo1,$bo1,$tok1) = twixt('(',')',$tok,$bo1);
 $cv = $tok1;
 logg($cv);
 list($fo2,$bo2,$cv) = twixt('',',',$cv,0);
 
 
lit-screenName( value=Customer1 ) 
 $tok = substr($disp,$fo,$bo-$fo);
 echo($tok);
/* lit-screenName( value=Customer1 ) */
 $fo = strpos($disp,"/*",$bo);
 $bo = strpos($disp,'*/',$fo);
 $tok = substr($disp,$fo,$bo-$fo+2);
 echo($tok);
/* text-userName() */