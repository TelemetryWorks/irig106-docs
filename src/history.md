# The Evolution of IRIG 106 Parsing: From C to Rust

For years, the telemetry community has relied on foundational C libraries, most notably the open-source `irig106lib`, to parse and process IRIG 106 Chapter 10 data. This library has served as the critical backbone for countless flight test programs and data analysis tools. It provided a highly portable, universally understood reference implementation for a complex standard.  
The architecture of `irig106lib` and similar legacy parsers is a product of its time and the paradigms of the C programming language. It follows a classic, stateful, function-dispatch model:  
1. Open a file handle.
2. Read the next header into memory.
3. Read the payload into a buffer.
4. Execute a massive `switch` statement on the data type.
5. Invoke the matching decoder function to fully unpack the payload into C structs.
While excellent for establishing a baseline of compatibility, this "monolithic parser" approach presents bottlenecks for modern, high-throughput workflows. It fundamentally tightly couples data traversal with data interpretation. In modern telemetry environments—where we are handling massive data lakes, streaming UDP ingest, and require rapid filtering—we rarely need to deeply decode every single payload. Often, a user simply wants to extract all MIL-STD-1553 messages from a specific channel within a tight time window. The legacy model forces the CPU to do unnecessary allocation and decoding work just to traverse the stream.  
This Rust implementation is not a 1:1 port of the C library. Instead, it is a ground-up reimagining of how to interact with Chapter 10 data, leveraging modern hardware capabilities and Rust's unique memory safety guarantees.  
