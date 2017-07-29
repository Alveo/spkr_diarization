import tools
import sad
import feat
import cluster
import bic

if __name__=='__main__':
    root_dir = './'
    out=tools.prepare_root(root_dir)
    wavname = tools.read_input()
    basename = tools.gen_uid(wavname)
    
    # SAD
#    sadname = '%s/%s_sad.txt'%(out,basename)
#    sad.run_sad(wavname,sadname)
#    
#    
#    # MFCC
#    featname = '%s/%s_feat.mfc'%(out,basename)
#    feat.run_mfcc(wavname,featname)
#    
#    # BIC
#    bicname = '%s/%s_bic.txt'%(out,basename)
#    bic.run_bic(featname,sadname,bicname)
#    
#    # CLUSTERING
#    clustname = '%s/%s_cluster.txt'%(out,basename)
#    cluster.run_clustering(featname,bicname,clustname)
#
#    
#    # Pick top clusters
#    labels, segment_starts,segment_ends = tools.read_segs(clustname)
#    top_n = tools.top_n_clustesr(labels, segment_starts,segment_ends)

    # TRAIN UBM
    ubmname = gmm.train(filelist,out)
#    for i in top_n:
#        cluster = 'C%s'%(str(i))
#        gmm.adapt(featname,clustname,cluster,ubmname)