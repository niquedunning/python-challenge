{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "file = \"../Resources/budget_data.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "------------------\n",
      "Total Months: 86\n",
      "Total Profit: $38382578\n",
      "Average Change: $7803.48\n",
      "Greatest Increase: Aug-2013, $999942\n",
      "Greatest Decrease: Aug-2012, $-1022534\n"
     ]
    }
   ],
   "source": [
    "with open('budget_data.csv', 'r') as f:\n",
    "    csvreader = csv.reader(f, delimiter = ',')\n",
    "    \n",
    "    header = next(csvreader)\n",
    "    \n",
    "    profitlist = []\n",
    "    monthlist = []\n",
    "    changelist = []\n",
    "    \n",
    "    months = 0 \n",
    "    profit = 0 \n",
    "    change = 0 \n",
    "    previous = 0\n",
    "    \n",
    "    for row in csvreader:\n",
    "        \n",
    "        months= months + 1\n",
    "        monthlist.append(row[0])\n",
    "        \n",
    "        profit = profit + int(row[1])\n",
    "        profitlist.append(row[1])\n",
    "        \n",
    "        \n",
    "        change = int(row[1]) - previous\n",
    "        changelist.append(change)\n",
    "        previous = int(row[1])\n",
    "\n",
    "        avgchange = sum(changelist)/len(changelist)\n",
    "        avgchangefinal = round(avgchange, 2)\n",
    "\n",
    "        gpandlinc = max(profitlist)\n",
    "        lgpandldec = min(profitlist)\n",
    "\n",
    "        highindex = profitlist.index(gpandlinc)\n",
    "        highdateindex = monthlist[highindex]\n",
    "        lowindex = profitlist.index(lgpandldec)\n",
    "        lowdateindex = monthlist[lowindex]\n",
    "print(\"Financial Analysis\")\n",
    "print(\"------------------\")\n",
    "print(f\"Total Months: {len(monthlist)}\")\n",
    "print(f\"Total Profit: ${profit}\")\n",
    "print(f\"Average Change: ${avgchangefinal}\")\n",
    "print(f\"Greatest Increase: {highdateindex}, ${gpandlinc}\")\n",
    "print(f\"Greatest Decrease: {lowdateindex}, ${lgpandldec}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('Output', 'w') as txt:\n",
    "    txt.write(\"Financial Analysis\")\n",
    "    txt.write(\"\\n------------------\")\n",
    "    txt.write(f\"\\nTotal Months: {len(monthlist)}\")\n",
    "    txt.write(f\"\\nTotal Profit: ${profit}\")\n",
    "    txt.write(f\"\\nAverage Change: ${avgchangefinal}\")\n",
    "    txt.write(f\"\\nGreatest Increase: {highdateindex}, ${gpandlinc}\")\n",
    "    txt.write(f\"\\nGreatest Decrease: {lowdateindex}, ${lgpandldec}\")"
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
