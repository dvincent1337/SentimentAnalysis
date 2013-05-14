SentimentAnalysis
=================

Python project: Analysis of sentiments from twiter (and perhaps other sources later)
                                                                  
  This project will attempt to compare happiness of terms in tweets.
  
  What you need:
  1) list of terms
  2) list of sentiments with sentiment values
  
  Demo walkthrough tutorial:
  
  This tutorial is comparing windows, mac, linux
  
  Steps:
    1) create list, download sentiment list
    2) download tweets
    3) analize the tweets
    4) review the data
    
    
    1) To create the list start a new text file called termList.txt with follwoing lines:
        windows
        mac
        linux
       Download AFINN-111.txt from http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010
    2) To download the tweets run the following command:
    
      python termDownload.py termList.txt > termData.txt
      
      The prevous command will save the tweet data in termData.txt, and output the progress to the screen.
      Wait unitl enough tweets have been downloaded then press ctl-c
      
    3) to analize the tweets run the following command
      
      python happiestTerm.py AFINN-111.txt termList.txt termData.txt
      
      after the program finishes you should recieve the output in Decending order. 
      here is a sample output run on ~880 thousand tweets
      
      Processing Item [884989]...
      Terms   Score	  Count	  PercentCount
      **************************************
      windows	0.7714	115646	43.0
      mac	    0.6085	85083	  32.0
      linux	  0.398	  62666	  23.0
      
    4) Review the data:
    
      Upon examining the data it looks like windows has the most happy results on average, however,
      there was about twice as many tweets in the data set about microsoft than there was about linux,
      so to make a better estimate, a paramater containing the max number of tweets to capture per term
      can be added when the program is executed. 
      
      For example to only allow 62500 tweets to be analized,
      run the following command
      
      python happiestTerm.py AFINN-111.txt termList.txt termData.txt 62500
      
      which on the dataset used in this example produced the following output:
      
      Processing Item [882725]...
      Terms    Score	Count	PercentCount
      **************************************
      windows	0.6712	62500	33.0
      mac	    0.5392	62500	33.0
      linux	  0.3927	62500	33.0
      
      Examining this data, it still shows that windows is regaurded as more happy than linux and mac, but the 
      score is a bit smaller than prevously
      
      So it looks like people that post to twitter are more happy about windows than they are about mac 
      and linux.
      
      Thanks for reading, and Happy Hacking!
      
      
