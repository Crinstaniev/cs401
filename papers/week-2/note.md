# Submission

## State-of-the-art

There are four generation of the intra-cluster network architecture before Jupiter. 

One of the early intra-cluster network architectures was called Four-Post Cluster Architecture, which had the advantage of being very simple to set up, but also the disadvantage of being very poorly scalable - once the entire cluster needed to be added or additional racks needed to be added, new routers needed to be added and each router needed to be connected to a new rack. Once the entire cluster needs to add servers or additional racks, new routers need to be added, and each router needs to be connected to the new rack. Many racks and servers are needed to fully utilize the 512 interfaces of the routers. High-Bandwidth App needs to be loaded in an entire Rack to avoid Oversubscription

The first generation of Google's network architecture was called Firehose 1.0, which did not go into use due to complex wiring, severe unreliability, and the above complexities, but brought experience and new ideas to subsequent designs.

The second generation of the architecture is called Firehose 1.1, and thanks to the new generation of Switch, the number of interfaces is directly doubled, which gives Firehose 1.1 a new architecture. Thanks to the two extra interfaces, the two ToRs are connected directly together, so that the overall Oversubscription Rate does not exceed 2 : 1. On the software side, the designers built a Control Plane to configure and manage the Single Board Computers (SBCs). The biggest problem was the connectivity between the servers.

Google's third-generation network is Watchtower. in order to reduce the complexity of the installation, Google has in line card will need to be connected to each server and switch chip, the external will be dense network connection line also packaged together, so as to greatly reduce the clutter of the network cable, but also reduce the chance of sending errors.

The fourth generation architecture is Saturn, which was created to cater to the growing number of servers and bandwidth requirements.

## Negative Points

The article presents an overview of the evolution of Google's intra-cluster network architecture, however, it lacks a critical component in providing a comprehensive analysis of the topic. The absence of a comparative analysis to other prominent industry players, such as Amazon, and relevant technologies diminishes the article's ability to provide an in-depth understanding of the subject matter. The inclusion of side-by-side comparisons would have enhanced the article's value by highlighting the unique and innovative aspects of Google's technology.

# Script

Before Google started to design their own datacenter network architecture, they use one of the traditional architecture which was called the Four-Post Cluster Architecture, which was easy to set up but not very scalable. As the scale of the cluster grew, new routers had to be added and connected to new racks, and many racks and servers were needed to fully utilize all interfaces of the routers. So Google decided to design their own. The Jupiter was the latest one, but before the Jupiter network architecture, there were four generations of intra-cluster network architecture. The first generation of Google's network architecture, Firehose 1.0, was not implemented due to complexity and reliability issues, but it provided valuable insights for future designs. The second generation, Firehose 1.1, doubled the number of interfaces and added a Control Plane to manage the Single Board Computers. However, the biggest challenge was still connectivity between servers. The third generation, Watchtower, reduced installation complexity by connecting line cards and switch chips directly to servers and packaging external network connections together. The fourth generation, Saturn, was designed to meet the demands of increasing numbers of servers and bandwidth needs.
