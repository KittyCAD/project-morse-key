# Product Design Document

| **Project:**      | Single Part Morse Key |
| ----------------- | --------------------- |
| **Author:**       | N McCleery            |
| **Release Date:** |                       |

## Summary

This document outlines the design process for a single part Morse key that employs a flexure hinge. That process indicates that a pure-PLA, FDM-printed key should be suitable. The part should have an upper arm section of 10mm x 3mm, with a cantilevered arm length of 80mm.

This design should provide for approximately 2mm of travel under 80gf actuation force, and offer a FoS of 16.

## Brief

### Product Description

A 'single part' straight Morse key body that employs a flexure hinge. This product should be considered a proof-of-concept intended for short duration demonstration purposes only.

### Initial Requirements

The product must:

- When actuated, close an electrical circuit.

- When released, return to its open 'home' position in a suitable timeframe.

- Require actuation force comparable to existing Morse keys or similar products.

- Provide sufficient mechanical durability for the intended product lifecycle.

- Include a stable base and/or appropriate mounting points to prevent unintended movement during operation.

### Constraints

The part must:

- Be manufacturable by FFF/FDM printing.
- Printed in PLA or PETG, or their CF-reinforced variants.
- Have total volume not exceeding 256x256x256mm.
- Have minimum wall thickness not less than 2mm.
- Have a maximum overhang angle of 45° without supports.

## Research & Requirements Development

### Key Topics

#### Actuation Force

Reference information for morse key actuation force was found to be sparse. However, available sources, [^1] [^2], list an adjustable morse key actuation range of 0-600gf, with fixed actuation of ≈240gf. Based on intuitive assessment, this magnitude of actuation force was felt to be greater than expected.

For comparison purposes, mechanical keyboard switches were investigated as alternative sources of actuation force data. Both Keychron [^3] and Cherry MX [^4] publish actuation force data for Cherry MX switch variants, and this data shows actuation forces ranging from ≈45gf to ≈80gf.

<center>
    <figure>
      <img src="./assets/01-cherry-mx-switches.png" alt="Cherry MX Key Actuation Force" style="width:75%">
      <figcaption>Fig. 1 - Cherry MX Switch Actuation Force</figcaption>
    </figure>
</center>
A hobbyist's blog post on the design of a manually milled morse key was also identified [^5]. Though the post's author does not provide a target actuation force, they do provide drawings and a nominal spring rate for the return spring employed in the design, from which actuation forces can be calculated.

Figure 2 shows that the design is a second class lever, with the return spring positioned between the pivot and the knob.

<center>
    <figure>
      <img src="./assets/02-hobbyist-design.png" alt="Hobbyist Morse Key Design" style="width:100%">
      <figcaption>Fig. 2 - Hobbyist Morse Key Design & Return Spring</figcaption>
    </figure>
</center>

Interrogation of the upper arm's drawing allows for relevant dimensions to be extracted and the system analysed.

<center>
    <figure>
      <img src="./assets/03-hobbyist-dims.png" alt="Hobbyist Morse Key Dimensions" style="width:100%">
      <figcaption>Fig. 3 - Hobbyist Morse Key — Critical Dimensions</figcaption>
    </figure>
</center>

Simplifying, a free body diagram for the second class lever system is as given in Figure 4:

<center>
    <figure>
      <img src="./assets/04-fbd.png" alt="Hobbyist Morse Key FBD" style="width:50%">
      <figcaption>Fig. 4 - Hobbyist Morse Key — FBD</figcaption>
    </figure>
</center>

The key designer lists the spring's free length, $lSpringFree$, as **14mm** and its rate, $kSpring$, as **0.93N/mm**. Further interrogation of the drawings also shows that the spring will be subject to 1mm of preload compression when fitted. Combining these values with the distances taken from the drawings, it becomes possible to compute the full set of target values:

$$
\begin{align}
&\text{Constants:} \nonumber \\[1em]
&l_{\text{Knob}} &= 44 \, mm \\
&_{\text{Spring}} &= 15 \, mm \\
&k_{\text{Spring}} &= 0.93 \, N/mm \\
&x_{\text{SpringPreload}} &= 1 \, mm \\[2em]

&\text{Apparent stiffness at knob:} \nonumber \\[1em]
&r_{\text{MechanicalAdvantage}} &= \frac{l_{\text{Knob}}}{l_{\text{Spring}}} = \frac{44 \, mm}{15 \, mm} = 2.93 \\
&k_{\text{Installed}} &= \frac{k_{\text{Spring}}}{r_{\text{MechanicalAdvantage}}^2} = \frac{0.93 \, N/mm}{2.93^2} = 0.108 \, N/mm \\[2em]

&\text{Force at knob to overcome spring preload:} \\[1em]
&F_{\text{Preload}} &= k_{\text{Spring}} \cdot x_{\text{SpringPreload}} = 0.93 \, N/mm \cdot 1 \, mm = 0.93 \, N \\
&F_{\text{PreloadKnob}} &= \frac{F_{\text{Preload}}}{r_{\text{MechanicalAdvantage}}} = \frac{0.93 \, N}{2.93} = 0.317 \, N
\end{align}
$$

As a confirmation step, mechanical advantage derived from lever arm length ratios can be compared with 'motion ratio' in terms of vertical displacement, $$x$$:

$$
\begin{align}
&\theta = 5^\circ &= 0.0873 \, rad \\
&x_{\text{Knob}} = l_{\text{Knob}} \cdot \sin(\theta) = 44 \, mm \cdot \sin(0.0873 \, rad) &= 3.83 \, mm \\
&x_{\text{Spring}} = l_{\text{Spring}} \cdot \sin(\theta) = 15 \, mm \cdot \sin(0.0873 \, rad) &= 1.31 \, mm \\
&r_{\text{Motion}} = \frac{x_{\text{Knob}}}{x_{\text{Spring}}} = \frac{3.83 \, mm}{1.31 \, mm} &= 2.93 \\[1em]
&r_{\text{Motion}}&=2.93\\
&r_{\text{MechanicalAdvantage}}&=2.93
\end{align}
$$

Finally, converting to gram-force in the interest of comparability with values above, this would equate to 32.3gf to overcome spring preload, with 11gf per mm of further travel—comparable in magnitude with the Cherry MX keyboard switch actuation force.

##### Recommendations

While the actuation force derived from [^5] broadly aligns with the Cherry MX switch data, commercially available morse keys are noted to have a stiffer operation. As a result, it is recommended that target actuation force for the nominal travel distance be set at the highest of the Cherry MX range: 80gf, or 0.78N.

#### Travel Distance

A preference for a gap of 0.2mm is noted in [^5], but the design could accommodate adjustment to a significantly larger value. [^6] recommends that novice morse key users set a contact spacing of between $1.5mm$ and $2mm$.

##### Recommendations

Given that novice users are advised to start with a contact spacing of ≈2mm, the finalised design should provide adjustable spacing that accommodates travel distance in the range [0mm, 2mm]—though larger gaps are acceptable.

#### Contact Options

Given the modest performance targets and initial requirements of the system, a simple steel fastener should be adequate. [^5] uses a contact pair that is composed of a conical point, stainless steel M4x10 and a socket head cap M3x16.

##### Recommendations

Stainless fastener contacts are assumed to be adequate for the system. Appropriate heat-set inserts may be required, though given that there will be no service load on the fasteners, tapped holes in the substrate may also be acceptable.

### Consolidated Requirements

Based on both the initial brief requirements and the outcome of the background work detailed above, categorised and consolidated product requirements are as follows:

#### Performance Requirements

P1. Must provide actuation force of 80gf (0.78N) at the knob.

P2. Must provide adjustable contact gap in range 0-2mm (larger gaps acceptable).

P3. Must return to open position when released.

P4. Return time should be "suitable" for Morse code operation.

P5. Contact spacing should be adjustable with recommended initial setting of ~2mm.

#### Electrical Requirements

E1. Must reliably close/open electrical circuit.

E2. Contacts should be stainless steel fasteners (M4×10 conical point and M3×16 socket head cap suggested).

E3. May use heat-set inserts or tapped holes for contact mounting.

#### Mechanical Requirements

M1. Must be stable during operation.

M2. Must include appropriate mounting points.

M3. Must provide sufficient mechanical durability for demonstration use.

M4. Must employ a flexure hinge design (as per product description).

#### Manufacturing Constraints

F1. Must be manufacturable by FFF/FDM printing.

F2. Must be printed in PLA, PETG, or their CF-reinforced variants.

F3. Maximum part volume: 256×256×256mm.

F4. Minimum wall thickness: 2mm.

F5. Maximum unsupported overhang angle: 45°.

F6. Must be manufacturable as a 'single part' (as per product description).

#### Integration

I1. Should support incorporation of fastener-based contacts.

I2. Should accommodate basic mounting/fastening requirements.

I3. Should accommodate potential incorporation of heat-set inserts if needed.

## Concept Development

### Concept Exploration

#### Concept 1

The first concept geometry employed a regular flexure (or living hinge design), using an arched and notched geometry as described in [^7], which would have to be 'folded' through ≈180° to reach its service position.

<center>
    <figure>
      <img src=".\assets\05-concept-01.png" alt="Concept 1" style="width:100%">
      <figcaption>Fig. 5 - Concept 1</figcaption>
    </figure>
</center>

Though this concept is thought be viable, the significant deformation between its as-manufactured and in-service geometry was considered likely to make simulation and verification of the design more challenging than necessary. It was also assumed that, though [^7] reports high fold cycle counts being achievable, that a design concept subject to less significant deformation would likely be more robust.

#### Concept 2

A simpler concept was sought, ideally allowing for more straightforward analytical assessment of stiffness, alongside more straightforward structural simulation. Accordingly, a simple C-shaped profile was chosen.

<center>
    <figure>
		<img src="./assets/06-concept-02.png" width=75%/>
        <figcaption>Fig. 6 - Basic Concept 2</figcaption>
    </figure>
</center>

This profile should allow for application of canitlevered beam analogy to guide rough sizing. In the event that the simple C-shaped profile cannot be rendered suitably compliant for the required strength, this concept can also be adapted to use a 'folded' approach, as demonstrated by [^8].

<center>
    <figure>
        <img src="./assets/07-folded.png" alt="Folded Flexure Design" width="50%" />
        <figcaption>Fig. 7 - Folded Cantilevered Flexure [8]</figcaption>
    </figure>
</center>

### Concept Selection

The C-section concept was modelled analytically as a cantilevered beam with rectangular section, point loaded at its extreme. Assuming a breadth of 10mm, peak deflection was computed for a range of beam depths and cantilever lengths, and for two materials. In all cases, applied force was assumed to be 0.78N.

The first material was Bambu Labs 'basic' PLA filament [^9]. The second was the carbon-fibre reinforced PLA variant [^10]. These offer properties as follows:

| Property \ Material | PLA            | PLA-CF         |
| ------------------- | -------------- | -------------- |
| Bending Modulus     | 2750 ± 160 MPa | 3950 ± 190 MPa |
| Bending Strength    | 76 ± 5 MPa     | 89 ± 4 MPa     |

<center>
    <figure>
        <img src="./assets/08-beam-deflection.png" alt="08-beam-deflection" />
        <figcaption>Fig. 8 - PLA Cantilever Deflection</figcaption>
    </figure>
</center>

<center>
    <figure>
        <img src="./assets/09-beam-deflection-cf.png" alt="09-beam-deflection-cf" />
        <figcaption>Fig. 9 - PLA-CF Cantilever Deflection</figcaption>
    </figure>
</center>

Based on these results, this concept is considered to be suitable when employing the basic PLA filament. A rectangular beam depth of around 3mm should provide 2mm of displacement, and the non-reinforced variant should be less likely to suffer a brittle failure mode.

## Design Development

Based on the analytical work conducted during concept exploration, design work was begun assuming the upper arm would adopt:

- An 80mm cantilever.
- A 3x10mm rectangular section.

In pure PLA, this was predicted to offer ~2mm of vertical displacement at the design load of 0.78N.

### Key Design Features

Beyond the cantilever dimension parameters, key features in the design were as follows:

1. A large internal radius at the cantilever root.
   - Included in the interest of minimising stress in the region where the system will be subject to bending. Though this feature was expected to reduce deformation at the upper arm's extremity under load, no further adjustment to arm geometry was made.
2. Mounting lug pads.
3. An integral knob for key operation.

<center>
    <figure>
        <img src="./assets/10-key-design-features.png" alt="Key Design Features" width="75%" />
        <figcaption>Fig. 10 - Key Design Features</figcaption>
    </figure>
</center>

Note that some features were not included at this stage due to software limitations, e.g., mounting fastener holes, contact arrangement holes, fillet radii at surface intersections etc.

### Material Selection

PLA was deemed most suitable. Bambu Labs PLA filament offers adequate performance.

### Manufacturing & Assembly Considerations

The part, as designed, is expected to require support structures during printing. Future reconfiguration of knob and mounting lug arrangement may permit some reduction in support material volume, but this is considered beyond the scope of this exercise.

Given that the part is intended to be subject to significant deformation in bending, print direction must be considered. For maximum bending strength, the part should be printed such that in-service bending load is applied perpendicular to print layers. For this part design, optimal general print direction is assumed to be parallel to the lever arm central axis, depositing filament in long horizontal passes[^11]. This approach would also ensure that shear loading does not induce delamination.

### Cost Considerations

Not applicable; part to be printed in-house from commodity filament, mated with commodity fasteners.

## Design Validation

### Analytical Methods

All analytical work conducted is described in [Concept Selection](#concept-selection); no further analytical validation was undertaken.

### FEA/CFD

[PrePomax](https://prepomax.fs.um.si/) [(Calculix)](https://www.calculix.de/) was used to validate the deflection values presented in Figure 8.

#### Methodology

Relevant features (mounting and contact holes) were first finalised with FreeCAD, then a STEP file was exported for use in PrePoMax. A simple model case was assembled as follows:

- Mesh: Second order tetrahedral throughout.
- Loads: A uniform pressure representing the design load (0.78N) applied to the top face of the knob.
- Boundary conditions: Fixed internal faces of mounting lug holes.
- Nonlinear geometric effects: Enabled.
- Material properties: As given in [Concept Selection](#concept-selection), with Poisson's Ratio assumed to be 0.3.

Note that subdivision of the model to facilitate regional mesh type changes and/or boundary condition refinement was not performed. In addition, the material was assumed to isotropic (see: [Limitations](#limitations)).

<center>
    <figure>
        <img src="./assets/11-model-case.png" alt="Model Case" />
        <figcaption>Fig. 11 - Model Case</figcaption>
    </figure>
</center>

#### Mesh Convergence

A simple mesh convergence exercise was completed:

- Iteration 1:

  - Max element size: 5mm.
  - Min element size: 2mm.

- Iteration 2:

  - Max element size: 2.5mm.
  - Min element size: 1mm.

- Iteration 3:

  - Max element size: 1.25mm.
  - Min element size: 0.5mm.

- Iteration 4:
  - Max element size: 0.625mm.
  - Min element size: 0.25mm.

Additionally, a model configured as in Iteration 3 had local mesh refinement applied, with element size reduced to 0.25mm around key features.

Mesh convergence results are shown in Figure 12, and local refinement is illustrated in Figure 13.

<center>
    <figure>
        <img src="./assets/12-mesh-convergence.png" alt="Mesh Convergence" />
        <figcaption>Fig. 12 - FEA Mesh Convergence</figcaption>
    </figure>
</center>

<center>
    <figure>
        <img src="./assets/13-local-refinement.png" alt="Local Mesh Refinement" />
        <figcaption>Fig. 13 - Local Mesh Refinement</figcaption>
    </figure>
</center>

#### Results

Iteration 4 and the locally refined Iteration 3 offer very close agreement in both peak deflection and maximum Von Mises stress. In both cases, simulated maximum deflection was ≈2.33mm. However, the node subject to maximum displacement relative to its starting point occurs at the knob extremity most distant from the key's hinge.

Inspection of nodes in the vicinity of the knob centerline indicates simulated deflection of ≈2.08mm, 96.7% of the value predicted analytically. Given that the analytical approach made no consideration of the radiused internal hinge, this is result is considered to validate the analytical method.

<center>
    <figure>
        <img src="./assets/14-max-deflection.png" alt="Max Deflection" />
        <figcaption>Fig. 14 - Iter. 4, Maximum Deflection</figcaption>
    </figure>
</center>

<center>
    <figure>
        <img src="./assets/15-max-deflection-node.png" alt="Max Deflection at Knob Centerline" />
        <figcaption>Fig. 15 - Iter. 3 Refined, Maximum Deflection at Key Node</figcaption>
    </figure>
</center>
The values provided by [^9] indicate a bending strength of 76±5MPa for the basic PLA filament. With respect to maximum bending stress, results indicate a peak Von Mises value of 4.346MPa—just 6% of the lower bound of the material's bending strength. This gives a factor of safety as follows:
$$
\begin{align}
\text{Maximum bending strength} &= 76 \pm 5 MPa \\
\text{Conservatively, } \sigma_{Max} &=71 MPa \\
\\
\text{Working Stress (FEA)} &= 4.346 MPa \\
\\
\text{ FoS} = \frac{71MPa}{4.346MPa} &= 16.3
\end{align}
$$

Given the high FoS, the design is considered unlikely to fail in bending. For illustrative purposes, simulated Von Mises stress is given in Figure 16.

<center>
    <figure>
        <img src="./assets/16-max-stress.png" alt="Max Stress" />
        <figcaption>Fig. 16 - Iter. 4, Maximum Von Mises Stress</figcaption>
    </figure>
</center>

## Conclusion

### Summary

The documented design process suggests that a pure-PLA, FDM-printed key should be viable. Its upper arm should be 10mm x 3mm, with a cantilevered arm length of 80mm.

This design should provide for approximately 2mm of travel under 80gf actuation force, and offer a FoS of 16.

### Limitations

#### Contacts

- Contact mechanics and wear were not considered.

#### Material Behaviour

- Materials assumed to be isotropic and ductile.
- Anisotropy arising from FDM print direction was not considered in analytical or finite element methods.
- No work was undertaken to investigate any non-solid infill pattern.
- Temperature effects were ignored.

#### Analysis

- Dynamic loading effects were ignored.
- Cycle and fatigue behaviour were not considered.

#### Manufacturing

- FDM layer adhesion strength variation not considered.
- Support structure impacts not considered.

### Further Work

#### Contacts

- Analyse contact mechanics and optimise contact geometry.
- Model contact wear mechanisms.
- Evaluate alternative fastener materials and geometries.

#### Material Analysis

- Characterise printed PLA anisotropy through testing.
- Investigate optimal infill patterns and densities.
- Map operating temperature effects.

#### FEA Refinement

- Implement hexahedral/transfinite mesh.
- Apply contact boundary conditions at mounting points.
- Incorporate anisotropic material properties.
- Model dynamic loading effects.

#### Manufacturing Development

- Optimise print orientation for layer adhesion.
- Develop support structure strategy.
- Test print parameter variations.
- Validate dimensional accuracy.

#### Validation

- Build and test prototype.
- Compare actual vs predicted deflection.
- Measure contact reliability.
- Document failure modes.

## Appendices

### Appendix A: Design Reviews

#### Design Review #1

Conducted on: YYYY-MM-DD

Key outcomes:

-

## References

[^1]: <https://www.ebay.co.uk/itm/264104597863> "https://www.ebay.co.uk/itm/264104597863"
[^2]: <https://www.eham.net/reviews/view-product?id=3214> "https://www.eham.net/reviews/view-product?id=3214"
[^3]: <https://www.keychron.com/blogs/news/cherry-mechanical-switch-guide> "https://www.keychron.com/blogs/news/cherry-mechanical-switch-guide"
[^4]: <https://www.cherry.de/en-gb/products/mx-switches/mx-standard> "https://www.cherry.de/en-gb/products/mx-switches/mx-standard"
[^5]: <https://www.giangrandi.ch/mechanics/cwsk/cwsk.shtml> "https://www.giangrandi.ch/mechanics/cwsk/cwsk.shtml"
[^6]: <https://www.electronics-notes.com/articles/ham_radio/morse_code/use-setup-straight-morse-key.php> "https://www.electronics-notes.com/articles/ham_radio/morse_code/use-setup-straight-morse-key.php"
[^7]: <https://sciendo.com/article/10.2478/bipcm-2022-0022> "https://sciendo.com/article/10.2478/bipcm-2022-0022"
[^8]: <https://www.esmats.eu/amspapers/pastpapers/pdfs/2024/carson.pdf> "https://www.esmats.eu/amspapers/pastpapers/pdfs/2024/carson.pdf"
[^9]: <https://uk.store.bambulab.com/products/pla-basic-filament> "https://uk.store.bambulab.com/products/pla-basic-filament"
[^10]: <https://uk.store.bambulab.com/products/pla-cf> "https://uk.store.bambulab.com/products/pla-cf"
[^11]: <https://www.protolabs.com/resources/blog/considerations-for-3d-printed-part-orientation/> "https://www.protolabs.com/resources/blog/considerations-for-3d-printed-part-orientation/"
