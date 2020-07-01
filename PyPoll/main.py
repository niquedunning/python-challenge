{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "import statistics\n",
    "file = \"../Resources/election_data.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "--------\n",
      "Total Votes: 3521001\n",
      "--------\n",
      "Khan: 2218231, 63.000%\n",
      "Correy: 704200, 20.000%\n",
      "Li: 492940, 14.000%\n",
      "O'Tooley: 105630, 3.000%\n",
      "--------\n",
      "Winner: Khan\n"
     ]
    }
   ],
   "source": [
    "#define variables\n",
    "totalvotes = 0\n",
    "khanvote = 0\n",
    "correyvote = 0 \n",
    "livote = 0\n",
    "otooleyvote = 0\n",
    "#define list\n",
    "votelist = []\n",
    "#import mode\n",
    "from statistics import mode \n",
    "#Open CSV Reader\n",
    "with open('election_data.csv','r') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter = ',')\n",
    "    \n",
    "    header = next(csvreader)\n",
    "    \n",
    "    for row in csvreader:\n",
    "        totalvotes = totalvotes + 1\n",
    "        \n",
    "        votelist.append(row[2])\n",
    "        \n",
    "    \n",
    "        if row[2]  == \"Khan\":\n",
    "            khanvote = khanvote + 1\n",
    "        elif row[2]  == \"Correy\":\n",
    "            correyvote = correyvote + 1\n",
    "        elif row[2]  == \"Li\":\n",
    "            livote = livote + 1\n",
    "        else:\n",
    "            otooleyvote = otooleyvote + 1\n",
    "            \n",
    "        vpkhan = khanvote / totalvotes\n",
    "        vpcorrey = correyvote / totalvotes\n",
    "        vpli = livote / totalvotes\n",
    "        vpotooley = otooleyvote / totalvotes\n",
    "        vpkhan = \"{:.3%}\".format(vpkhan)\n",
    "        vpcorrey = \"{:.3%}\".format(vpcorrey)\n",
    "        vpli = \"{:.3%}\".format(vpli)\n",
    "        vpotooley = \"{:.3%}\".format(vpotooley)\n",
    "        votelist.append(row[2])\n",
    "        def winner(votelist):\n",
    "            return(mode(votelist))\n",
    "            \n",
    "print(\"Election Results\")\n",
    "print('--------')\n",
    "print(f\"Total Votes: {totalvotes}\")\n",
    "print('--------')\n",
    "print(f\"Khan: {khanvote}, {vpkhan}\")\n",
    "print(f\"Correy: {correyvote}, {vpcorrey}\")\n",
    "print(f\"Li: {livote}, {vpli}\")\n",
    "print(f\"O'Tooley: {otooleyvote}, {vpotooley}\")\n",
    "print('--------')\n",
    "print(f'Winner: {winner(votelist)}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "electionresults = os.path.join(\"electionresults.txt\")  \n",
    "\n",
    "with open('election', 'w') as txt:\n",
    "    txt.write(\"Election Results\")\n",
    "    txt.write('\\n--------')\n",
    "    txt.write(f\"\\nTotal Votes: {totalvotes}\")\n",
    "    txt.write('\\n--------')\n",
    "    txt.write(f\"\\nKhan: {khanvote}, {vpkhan}\")\n",
    "    txt.write(f\"\\nCorrey: {correyvote}, {vpcorrey}\")\n",
    "    txt.write(f\"\\nLi: {livote}, {vpli}\")\n",
    "    txt.write(f\"\\nO'Tooley: {otooleyvote}, {vpotooley}\")\n",
    "    txt.write('\\n--------')\n",
    "    txt.write(f'\\nWinner: {winner(votelist)}')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
