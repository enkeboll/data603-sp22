from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col
from pyspark.sql.functions import split

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

# Create DataFrame representing the stream of input lines from connection to localhost:9999
lines = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

# Split the lines into words
# words = lines.select(
#    explode(
#        split(lines.value, " ")
#    ).alias("word")
# )

# # Generate running word count
# wordCounts = words.groupBy("word").count()

# Filter out non-TB tweets
tb_mesages = lines.filter(col("value").contains("taco bell"))


 # Start running the query that prints the running counts to the console
query = tb_mesages \
    .writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("checkpointLocation", "checkpoint/") \
    .option("path", "class07_output/") \
    .trigger(processingTime="4 second") \
    .start()

query.awaitTermination()
