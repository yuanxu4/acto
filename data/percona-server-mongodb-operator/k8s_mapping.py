import known_schemas

WHITEBOX = [
    known_schemas.K8sField(['spec', 'backup', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'backup', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'backup', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'backup', 'image'], known_schemas.ImageSchema),
    known_schemas.K8sField(['spec', 'backup', 'runtimeClassName'], known_schemas.K8sStringSchema),
    known_schemas.K8sField(['spec', 'backup', 'serviceAccountName'], known_schemas.ServiceAccountNameSchema),
    known_schemas.K8sField(['spec', 'backup', 'tasks', 'ITEM', 'schedule'], known_schemas.CronJobScheduleSchema),
    known_schemas.K8sField(['spec', 'image'], known_schemas.ImageSchema),
    known_schemas.K8sField(['spec', 'imagePullPolicy'], known_schemas.ImagePullPolicySchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'nodeSelector'], known_schemas.NodeSelectorSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'podDisruptionBudget'], known_schemas.PodDisruptionBudgetSpecSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'priorityClassName'], known_schemas.PriorityClassNameSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'volumeSpec', 'persistentVolumeClaim', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'volumeSpec', 'persistentVolumeClaim', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'volumeSpec', 'persistentVolumeClaim', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'volumeSpec', 'persistentVolumeClaim', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'tolerations'], known_schemas.TolerationsSchema),
]

BLACKBOX = [
    known_schemas.K8sField(['spec', 'backup', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'backup', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'backup', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'arbiter', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'nonvoting', 'volumeSpec', 'persistentVolumeClaim', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'replsets', 'ITEM', 'volumeSpec', 'persistentVolumeClaim', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'volumeSpec', 'persistentVolumeClaim', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'tolerations'], known_schemas.TolerationsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'configsvrReplSet', 'volumeSpec', 'persistentVolumeClaim', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'affinity', 'advanced'], known_schemas.AffinitySchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'containerSecurityContext'], known_schemas.SecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'podSecurityContext'], known_schemas.PodSecurityContextSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'sidecarPVCs', 'ITEM', 'spec', 'resources'], known_schemas.ResourceRequirementsSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'sidecarVolumes', 'ITEM'], known_schemas.VolumeSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'sidecars', 'ITEM'], known_schemas.ContainerSchema),
    known_schemas.K8sField(['spec', 'sharding', 'mongos', 'tolerations'], known_schemas.TolerationsSchema),
]